from kirje import Kirje, KirjeDetails
print("Show mock List of messages in streamlined style:")
details = KirjeDetails(
    headers={
        'ID': 'Title',
        'Title': ' notes ',
    },
    content="1 - example\n2 - tomorrow",
    header_separation=" - "
)

message = Kirje(details)
message.display("streamlined")

print("\nShow mock note in default style:")
details = KirjeDetails(
    headers={
        'ID': 2,
        'Title': 'tomorrow',
        
    },
    content="eat\nstudy\nsleep",
    header_separation=" - "
)

message = Kirje(details)
message.display("default")