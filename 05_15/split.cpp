#include <vector>
#include <string>
#include <iostream>

bool isspace(char c)
{
    return c == ' ' || c == '\n' || c == '\t';
}

std::vector<std::string>
    my_split(std::string str, char sep = ' ') {
        std::vector<std::string> result;
        
        std::string temp = "";
        for (int i = 0; str[i] != '\0'; ++i)
        {
            if (str[i] != sep || !isspace(str[i]))
            {
                temp += str[i];
            }
            else if (!temp.empty())
            {
                result.push_back(temp);
                temp = "";
            }
        }
        if (!temp.empty())
            result.push_back(temp);
        return result;
}


int count_w(const char *str, char sep)
{
    int count = 0;
    bool isSpace = true; 
    for (size_t i = 0; str[i] != '\0'; i++)
    {
        if (str[i] != sep || !isspace(str[i]))
        {
            if (isSpace)
            {
                ++count;
                isSpace = false;
            }
        } else {
            isSpace = true;
        }
    }
    return count;
}

int count_char_in_w(const char *str, char sep)
{
    int len = 0;
    while (str[len] != sep || !isspace(str[len]))
    {
        ++len;
    }
    return len;
}

char **my_split(const char *str, char sep = ' ')
{
    char **split_str = new char*[count_w(str, sep) + 1];

    char *tmp = new char[count_char_in_w(str, sep)]; 

    return split_str;
}

int main(int argc, char const *argv[])
{
    std::string test = "My name is Mike";

    // auto split_test = my_split(test);
    // for (   auto i = split_test.begin();
    //         i != split_test.end();
    //         i++) {
    //             std::cout << *i << "\n";
    // }
    

    std::cout << count_w("My     name is\n Mike", ' ') << "\n";

    return 0;
}
