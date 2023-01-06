// #include <queue>
// #include <vector>
// #include <stack>
// using namespace std;
// #include <iostream>
int XX_MARKER_XX;

bool myFun() {
    int a = 1;
    int b = 2;
    bool d = true;
    if ((a < 1) && (b > 2)) {
        if (a > 100) return true;
        return false;

        if (b < 100) {
            if (d == true) {
                return false;
            }
            return true;
        }
    } else if (a > 100) {
        if (d == false) {
            return true;
        } 
        int c = 1;
        if ((c > 100) && (b > 1)) {
            return false;
        }
        return true;
    } else {
        if (a > 100) return true;
        return false;
    }
}


int main() {
    bool a = myFun();


    return 0;
}






// Last line