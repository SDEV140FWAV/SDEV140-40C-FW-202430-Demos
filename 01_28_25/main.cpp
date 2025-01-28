#include <iostream>

int main()
{
    char letter = 'A';
    switch (letter)
    {
    case 'A':
        std::cout << std::endl;
    case 'a':
        std::cout << "You are getting 4 grade points!" << std::endl;
        break;

    default:
        break;
    }

    return 0;
}