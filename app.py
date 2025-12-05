import gradio as gr

class SortingState:

    def __init__(self):

        print("state class")
    

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