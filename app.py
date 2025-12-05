import gradio as gr
import random

# Core Insertion Sort Logic
class SortingState:

    def __init__(self):

        # Initialize array values
        # 8 Elements, each a random number between 10 and 99
        self. arr = [random.randint(10, 99) for num in range(8)]

        # Sorting indices for insertion sort
        # i: The element we are currently trying to insert into the sorted portion
        # j: The index we are currently comparing against (i-1 down to 0)
        self.i = 1
        self.j = 0

        # Track when array is fully sorted
        self.sorting_complete = False

def generate_html_view(state):
    """
    Creates a colourful HTML representation of the array.
    """
    html = '<div style="display: flex; justify-content: center; align-items: flex-end; height: 300px; gap: 10px; font-family: sans-serif;">'
    
    max_val = max(state.arr) if state.arr else 100
    
    for index, val in enumerate(state.arr):
        
        # 20 as the minimum height, add height by value's percent of the maximum value
        height = 20 + (val / max_val) * 80
        
        # Default Style
        colour = "#3b82f6" # Blue (Unsorted)
        border = "none"
        label_colour = "white"
        transform = "none"
        z_index = "1"
        box_shadow = "none"
        
        if state.sorting_complete:
            colour = "#10b981" # Green (Done)
        else:
            #  Logic based on Insertion Sort Phase
            
            if index < state.i:
                colour = "#60a5fa" # Lighter Blue (processed)

            # The element the sorting key
            if index == state.j + 1:
                colour = "#f59e0b" # Orange (The Key)
                transform = "scale(1.1)"
                z_index = "10"
                box_shadow = "0px 0px 15px rgba(245, 158, 11, 0.6)"

            # The element being compared against
            elif index == state.j:
                colour = "#ef4444" # Red (Comparison Target)

        # Generate the HTML of each array element
        html += f"""
        <div style="
            height: {height}%; 
            width: 60px; 
            background-colour: {colour}; 
            border: {border};
            border-radius: 8px 8px 0 0;
            display: flex; 
            flex-direction: column;
            justify-content: flex-end;
            align-items: center;
            font-weight: bold;
            colour: {label_colour};
            font-size: 1.2rem;
            padding-bottom: 10px;
            transition: all 0.3s ease;
            transform: {transform};
            z-index: {z_index};
            box-shadow: {box_shadow};
        ">
            {val}
            <span style="font-size: 0.8rem; opacity: 0.7; font-weight: normal; margin-top: 5px;">idx:{index}</span>
        </div>
        """
    html += '</div>'
    return html


def process_decision(user_input, state):
    """
    Takes in the user input left or stay
    Takes in the state of the SortingState class
    """

    # If sorting finished, generate finished HTML
    if state.sorting_complete: 
        return state, generate_html_view(state), "Sort Finished", "Please reset to start over."
    

    # Insertion sort logic
    key = state.arr[state.j + 1]
    left_idx = state.j

    # The correct swap decision
    should_swap = key < state.arr[left_idx]

    # True if user decides to swap
    user_swap = (user_input == "Swap (Move Left)")

    # For the GUI
    feedback = ""

    if user_swap == should_swap:

        # If user is correct (swap is the right choice)
        if should_swap:

            # Perform swap
            state.arr[state.j], state.arr[state.j + 1] = state.arr[state.j + 1], state.arr[state.j]
            feedback = "Correct! The key is smaller, so it moves left."
            
            if state.j > 0:
                state.j-=1
            else:
                feedback += "Reached the start; next element!"
                state += 1
                state.j = state.i - 1
        
        # If user is correct (no swap is the right choice)
        else:
            feedback = "Correct; the key is in the right spot for this iteration."
            state += 1
            state.j = state.i - 1

        # Check if entire sort is finished (when i reaches the end)
        if state.i >= len(state.arr):
            state.sorting_complete = True
            feedback = "Sorting Complete!"

    # User made the wrong decision
    else:
        if should_swap:
            feedback = f"Incorrect. {key} is smaller than {state.arr[left_idx]}, so we should swap the elements."
        else:
            feedback = f"Incorrect. {key} is NOT smaller than {state.arr[left_idx]}, so we don't move it."

    return state, generate_html_view(state), state.get_current_status(), feedback







    
def reset_game(array):
    new_state = SortingState(array)
    return (
        new_state, 
        generate_html_view(new_state), 
    )

    

# Initialize gradio interface
with gr.Blocks(title="Interactive Selection Sort", theme=gr.themes.Soft()) as demo:

    game_state = gr.State(SortingState())

    gr.Markdown("""
    # Interactive Insertion Sort
    Help sort the array using **Insertion Sort**.
    
    **Rules:**
    1. Look at the **Orange Bar** (The Key).
    2. Look at the **Red Bar** (The Neighbor to the left).
    3. Decide: Should the Orange Bar move left? (Is Orange less than Red?)
    """
    )




demo.launch()