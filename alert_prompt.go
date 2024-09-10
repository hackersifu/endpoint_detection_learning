package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Display the T1082 message to the user
	fmt.Println("T1082 is happening!")

	// Display the prompt to press any key
	fmt.Println("Press any key to close this window...")

	// Create a new reader to capture the user's input
	reader := bufio.NewReader(os.Stdin)

	// Read a single byte (any key press) from the input
	_, _ = reader.ReadByte()
}
