 

#1 Simple Python Calculator  

This project is a simple console-based calculator program written in Python. It allows users to perform basic arithmetic operations, including addition, subtraction, multiplication, and division.  

## Features  
- **Addition**: Add two numbers.  
- **Subtraction**: Subtract the second number from the first.  
- **Multiplication**: Multiply two numbers.  
- **Division**: Divide the first number by the second.  

## How It Works  
1. The program displays a menu with the following options:  
   ```
   1 - ADD  
   2 - SUBTRACT  
   3 - MULTIPLY  
   4 - DIVIDE  
   ```  
2. The user selects an option by entering the corresponding number.  
3. The program prompts the user to enter two numbers for the operation.  
4. Based on the selected option, the program performs the operation and displays the result.  
5. If an invalid option is selected, the program outputs an error message.  

## Example Usage  
```
1 - ADD  
2 - SUBTRACT  
3 - MULTIPLY  
4 - DIVIDE  

Select an operation to perform: 1  
Enter first number: 5  
Enter second number: 3  
Result is 8.0  
```  

## Prerequisites  
- Python 3.x installed on your system.  

## Running the Program  
1. Clone or download this repository.  
2. Navigate to the directory containing the script.  
3. Run the program using the following command:  
   ```
   python calculator.py  
   ```  

## Notes  
- Ensure that the inputs are valid numbers.  
- Division by zero is not handled explicitly and will raise an error.  

### README.md  

#2 Number Guessing Game  

This project is a simple Python-based number guessing game. The program generates a random number within a range specified by the user and challenges the player to guess the number. The game provides hints if the player's guess is too high or too low until they guess correctly.  

## Features  
- Generates a random number between 1 and a user-defined upper limit.  
- Provides feedback on each guess:  
  - "Too Low" if the guess is less than the random number.  
  - "Too High" if the guess is greater than the random number.  
- Congratulates the player when they guess the correct number.  

## How It Works  
1. The program selects a random number within the range of 1 to `x` (where `x` is specified by the user in the code).  
2. The player repeatedly guesses the number until they get it right.  
3. After each incorrect guess, the program provides feedback to guide the player.  

## Example Usage  
```
Guess a number between 1 and 100: 50  
Too Low, Please try again.  
Guess a number between 1 and 100: 75  
Too High, Please try again.  
Guess a number between 1 and 100: 62  
Congratulations, You have guessed the number 62  
```  

## Prerequisites  
- Python 3.x installed on your system.  

## Running the Program  
1. Clone or download this repository.  
2. Navigate to the directory containing the script.  
3. Run the program using the following command:  
   ```
   python guessing_game.py  
   ```  

## Customization  
- Modify the `guess(x)` function call at the end of the script to set the upper limit of the range. For example:  
  ```python
  guess(50)  # Sets the range from 1 to 50.  
  ```  

## Notes  
- Ensure to input valid integers when prompted.  
- The game handles only numeric inputs within the specified range.  
 
