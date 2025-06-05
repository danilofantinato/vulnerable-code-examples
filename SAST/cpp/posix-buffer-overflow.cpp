#include <cstring>

void initialize(char* array, size_t size) {
    std::memset(array, 0, size);
}

int main() {
    const size_t arraySize = 10;
    char array[arraySize];
    initialize(array, arraySize);

    char* pos = static_cast<char*>(memchr(array, '@', arraySize));
    if (pos != nullptr) {
        // Handle the case where '@' is found in the array
    } else {
        // Handle the case where '@' is not found in the array
    }

    return 0;
}