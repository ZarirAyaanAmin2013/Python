undo_stack = []
redo_stack = []

undo_stack.append("typed 'hello'")
undo_stack.append("deleted '0'")
print("undo:", undo_stack)
last_action = undo_stack.pop()
redo_stack.append(last_action)
print("undo:", last_action)
print("undo:", redo_stack)
redo_action = redo_stack.pop()
undo_stack.append(redo_action)
print("redo:", redo_action)
