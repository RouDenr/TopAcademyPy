#include <iostream>

int numlen(int n)
{
    int len = 1;
    while (n / 10 != 0)
    {
        ++len;
        n /= 10;
    }
    return len;
}

char *itos(int n)
{
    int len = numlen(n);
    bool isNegative = false;
    if (n < 0)
    {
        ++len;
        n *= -1;
        isNegative = true;
    }
    char *str = new char[len + 1];
    str[len] = '\0';


    int tmp = n;
    int i = len - 1;
    if (isNegative)
    {
        str[0] = '-';
    }
    while (tmp != 0)
    {
        str[i] = tmp % 10 + '0';
        tmp /= 10;
        i--;
    }

    return str;
}

int main(int argc, char const *argv[])
{
    int n = -26;

    std::cout << itos(n) << "\n";
    return 0;
}
