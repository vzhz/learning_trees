tree = {
	"a":["b", "e"],
	"b": ["c", "d"],
	"c": [],
	"d": [],
	"e": []
	}

#a = root
#4 spaces in python is com. standard, editor can confert tab to spaces
#read pep8



def traverse(tree):
	current_node = "a"
	stack = [] #append and pop for stack, append and popleft for que
	seen = set()
	stack.extend(tree[current_node]) #extend contactonates lists, note order is same as in lists  
	while len(stack) != 0: #while stack is alernate bc "truthy" and "falsy"
		print current_node, stack
		current_node = stack.pop()
		print current_node, stack
		if current_node in seen:#graph not tress because of this
			continue #pops back to top of while
		seen.add(current_node)
		stack.extend(tree[current_node])

traverse(tree)
