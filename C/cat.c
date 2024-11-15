#include <stdio.h>

#define LINE_LENGTH 10000



int main(int argc, char *argv[]){
    // printf("Hello World\n");
    // printf("This is the number of arguments: %d\n",argc);
    // printf("These are the arguments:\n");

    FILE *file;
    char line[LINE_LENGTH];

    for (int i = 1; i < argc; i++) {
        printf("%s\n", argv[i]);

        file = fopen(argv[i],"r");


        if (file == NULL) {
            printf("Error opening file: %s\n", argv[i]);
        }
        while (fgets(line, LINE_LENGTH, file) != NULL){
            printf("%s",line);
        }

        fclose(file);
    }

    
    
}