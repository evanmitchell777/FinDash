#include <iostream>
#include <string>
#include <httplib.h>
 
using namespace std;

class Stock{
public: 
    string ticker;
    int dataLength; //contains num of days stock data is available for

    Stock(string ticker){
        this->ticker;
        this->dataLength;
            std::string symbol = "AAPL";  // Example stock symbol

        // Build the URL for fetching the historical data
        std::string url = "/v8/finance/chart/" + symbol + "?interval=1d";
        std::string host = "query1.finance.yahoo.com";
        std::string endpoint = "https://" + host + url;

        // Create an HTTP client
        httplib::Client client(host.c_str());

        // Send the GET request
        auto response = client.Get(url.c_str());
        if (response && response->status == 200) {
            // Parse the JSON response
            nlohmann::json jsonData = nlohmann::json::parse(response->body);

            // Extract the historical data
            const auto& timestamps = jsonData["chart"]["result"][0]["timestamp"];
            const auto& prices = jsonData["chart"]["result"][0]["indicators"]["quote"][0]["close"];

            // Print the historical data
            for (std::size_t i = 0; i < timestamps.size(); ++i) {
                long long timestamp = timestamps[i].get<long long>();
                double price = prices[i].get<double>();
                std::cout << "Timestamp: " << timestamp << ", Price: " << price << std::endl;
            }
        }
        else {
            std::cout << "Request failed: " << (response ? response->status : -1) << std::endl;
        }

    };

    
}
