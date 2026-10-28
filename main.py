from pyscript import display, document


def process_registration(evt_data):
    """Processes user input to add a new member and updates the roster using set operations."""
    
    # Clear previous screen output
    document.getElementById('roster_box').innerHTML = " "

    # Predefined sets containing famous celebrity names
    frosh_group = {'Taylor Swift', 'Bruno Mars', 'Ed Sheeran'}
    soph_group = {'Zendaya Coleman', 'Tom Holland', 'Timothée Chalamet', 'Florence Pugh'}
    jun_group = {'LeBron James', 'Stephen Curry', 'Kevin Durant'}
    sen_group = {'Bill Gates', 'Elon Musk', 'Mark Zuckerberg', 'Steve Jobs'}

    # Retrieve user inputs from the HTML form
    user_given_name = document.getElementById('fname_input').value
    user_sur_name = document.getElementById('lname_input').value

    # Combine names and structure into a single-element set
    entry_full_name = user_given_name + " " + user_sur_name
    entry_member_set = {entry_full_name}

    # Combine all student sets using the set union (|) operator
    combined_master_set = frosh_group | soph_group | jun_group | sen_group | entry_member_set
    
    # Calculate total count of unique members across all sets
    tally_count = len(frosh_group | soph_group | jun_group | sen_group | entry_member_set)

    # Format sorted member names with line breaks for web presentation
    formatted_roster_str = "<br>".join(sorted(combined_master_set))

    # Render full member list and total count to the DOM output container
    document.getElementById('roster_box').innerHTML = f'All members:<br>  {formatted_roster_str}'
    display(f'Total members: {tally_count}', target='roster_box')