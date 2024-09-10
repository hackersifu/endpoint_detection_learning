package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("T1082 is happening!")
	fmt.Println("Press any key to close this window...")

	reader := bufio.NewReader(os.Stdin)
	_, _ = reader.ReadByte()
}
