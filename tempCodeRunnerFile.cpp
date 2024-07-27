#include <iostream>
#include <cmath>

using namespace std;

class COCOMO_Basic {
private:
    const double A = 2.8;   // COCOMO Basic exponent
    const double B = 1.20;  // COCOMO Basic exponent
    const double TDEV = 2.5; // Development time exponent

public:
    void calculate(double KLOC) {
        // Calculate Effort
        double Effort = A * pow(KLOC, B);

        // Calculate Time to Development
        double Time = TDEV * pow(Effort, 0.33);

        // Calculate Productivity
        double Productivity = KLOC / Effort;

        // Output the results
        cout << "Effort (person-months): " << round(Effort * 100) / 100 << endl;
        cout << "Time to Development (months): " << round(Time * 100) / 100 << endl;
        cout << "Productivity (KLOC/person-month): " << round(Productivity * 100) / 100 << endl;
    }
};

int main() {
    COCOMO_Basic model;
    double KLOC;

    // Input KLOC
    cout << "Enter the size of the software project in KLOC (thousands of lines of code): ";
    cin >> KLOC;

    // Calculate using COCOMO Basic Model
    model.calculate(KLOC);

    return 0;
}
