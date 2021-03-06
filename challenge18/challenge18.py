"""
In this Bite you complete print_hanging_indents to print a poem (or text) in
a nicer way.

For example calling it on (part of) Christina Rosetti's Remember it
should convert:

                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
to:
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
That's it! The tests include another text snippet from Shakespeare. Have fun!
"""

INDENTS = 4


def print_hanging_indents(poem):
    """You can use textwrap's fill but this worked better for us"""
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines()
                 if line.strip()]
        print(lines[0])
        for line in lines[1:]:
            print(' ' * INDENTS + line)
