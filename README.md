# Insertion Sort Interactive Application
## Description
The application provides a user with an interactive walk through of the logical steps involved in the insertion sort algorithm. By looping through the array, and making ```swap``` or ```stay``` decisions, the user eventually will sort the numerical array in order. This provides a visual illustration of a coding algorithm, providing insight and education to the reason why insertion sort works and its potential pitfalls in memory and time complexity.
## Design 
This app uses a gradio python interface to display an interactive web UI. By using inline HTML, I was able to customize the design of the interface with colours, height and CSS flex box containers. To implement the insertion sort design, I used a ```SortingState``` class which holds the status and values of the array to be storted. For the specific logic, I used a ```process_decision``` function which takes in the current ```state``` and the ```user_input```. Given these two variables, the user input is deemed as correct or wrong, returns feedback, and adjusts the array accordingly. The application also allows for a user inputed array with a gradio input box which calls the ```reset_game``` functions. 

## Algorithmic Thinking Pillars
### Pattern Recognition
I applied my experience with react ```redux``` states to create a similar ```SortingState``` object which holds the universal array values. 

### Decomposition
I focused on splitting the sections of the applications into seperate functions. For HTML design, I used the ```generate_html_view``` function. For the core insertion sort logic, the ```process_decision``` function. And for the array storage, the ```SortingState``` class.

