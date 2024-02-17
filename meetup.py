import streamlit as st


# Set the page to use a wide layout
st.set_page_config(layout="wide")

# Sample data structure for events
events = [
    {"title": "In-Person Group Meditation", "host": "Hingham Guided Meditation Meetup Group",
     "date": "THU, FEB 29 - 7:00 PM EST", "attendees": 1, "image": "meditation.jpg", "is_free": True},
    {"title": "International friends Boston", "host": "International friends Boston",
     "date": "TUE, FEB 20 - 7:00 PM EST", "attendees": 128, "image": "international_friends.jpg", "is_free": True},
    # ... Add two more events to make it four
    {"title": "Event Title 3", "host": "Host 3",
     "date": "DATE 3", "attendees": 30, "image": "image3.jpg", "is_free": False},
    {"title": "Event Title 4", "host": "Host 4",
     "date": "DATE 4", "attendees": 45, "image": "image4.jpg", "is_free": True},
]

# Display the title and location
st.title("Events near Dorchester, MA")

# Create a row of four columns for the events
cols = st.columns(4)  # Now we have four columns in one row

# Iterate over the events and the columns simultaneously using zip
for col, event in zip(cols, events):
    with col:
        # The image path below assumes images are hosted online. Replace with your actual image paths.
        # Placeholder for actual image URLs
        image_path = f"https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2/{event['image']}"
        st.image(image_path, use_column_width=True)
        st.subheader(event["title"])
        st.caption(f"Hosted by: {event['host']}")
        st.caption(event["date"])
        attendees = f"{event['attendees']} going" if event['attendees'] > 1 else "1 person going"
        st.markdown(attendees)
        st.markdown("Free" if event["is_free"] else "Paid")
        st.button("Join", key=f"join_{event['title']}")

# The 'See all events' button can be placed below the events
st.button("See all events")
