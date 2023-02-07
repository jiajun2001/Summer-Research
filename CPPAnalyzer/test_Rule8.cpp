int XX_MARKER_XX;

int main(void) {
    int a = 1;

    if (a == 3) {
       a = 1;
    } else {
        double c = 1;
        a = a;
        int b = 1;
        if (false) {
            c = c;
            if (a == 1) {
                a = a;
            } else if (c == 1) {
                a++;
            } else {
                b = b;
                a++;
            }
        }
    }   
}