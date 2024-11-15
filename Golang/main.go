package main

import (
	"errors"
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e != nil {

		if errors.Is(e, os.ErrNotExist) {
			println("file does not exit")
		} else {
			panic(e)

		}

	}
}

func main() {
	fileNames := os.Args[1:]

	fmt.Println(fileNames)

	cwd, err := os.Getwd()

	if err != nil {
		fmt.Println("Error getting workind directory:", err)
	}

	for _, fileName := range fileNames {
		fmt.Println(fileName)

		file := filepath.Join(cwd, fileName)

		fileAbsPath, err := filepath.Abs(file)

		if err != nil {
			fmt.Println("Error getting absolute path:", err)
		}

		fmt.Println("Full path for the files is: ", fileAbsPath)

		fileContent, err := os.ReadFile(fileAbsPath)
		check(err)

		//fmt.Println(string(fileContent))

		os.Stdout.Write(fileContent)

	}

}
