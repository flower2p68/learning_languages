#include <iostream> 
using namespace std;

int main() {
    int n = 8;
    int m[8][8];

    for (int i = 0; i < n; i++) {
        int inicio = 1;
        if (i % 2 == 0) {
            inicio = 0;
        }
        for (int j = 0; j < n; j++) {
            m[i][j] = inicio;
            inicio = 1 - inicio;
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
