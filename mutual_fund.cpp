/* To do: make it to where information is pulled from stored set location that is changed by python program.
Add Graphing */
#include <iostream>
using namespace std;

class Fund {
public:
    string fund_name;
    float YTD;
    float one_year_performance;
    float three_year_performance;
    float five_year_performance;
    float ten_year_performance;
    float dividend;
    
    Fund(string fund_name, float YTD, float one_year_performance, float three_year_performance, float five_year_performance, float ten_year_performance, float dividend) {
        this->fund_name = fund_name;
        this->YTD = YTD;
        this->one_year_performance = one_year_performance;
        this->three_year_performance = three_year_performance;
        this->five_year_performance = five_year_performance;
        this->ten_year_performance = ten_year_performance;
        this->dividend = dividend;
    }
    
    string getName() {
        return fund_name;
    }
    
    float getYTD() {
        return YTD;
    }
    
    float getOne_year() {
        return one_year_performance;
    }
    
    float getThree_year() {
        return three_year_performance;
    }
    
    float getFive_year() {
        return five_year_performance;
    }
    
    float getTen_year() {
        return ten_year_performance;
    }
    
    float getDividend() {
        return dividend;
    }
};

int main() {
    Fund fund_1("VFIAX", 8.36, 10.5, 12.8, 15.2, 18.6, 2.5);

    cout << fund_1.getName() << endl;
    return 0;


Fund fund_2("FFFHX",10.3,11.7,20,11,11,11);
}
