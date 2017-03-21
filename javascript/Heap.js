function Node (data) {
    this.data = data;
    this.left = null;
    this.right = null;
    this.parent_node = null;
}

function Heap (root) {
    this.root = root;
    this.current_level = [root];
    this.current_ind = 0;
    this.current_node = this.current_level[this.current_ind];
}

Heap.prototype.set_current_node = function() {
    this.current_node = this.current_level[this.current_ind];
}

Heap.prototype.place_value_recurse = function(node, parent_node) {
    if (node.data < parent_node.data) {
        // Switch the values and make the recursive call
        saved_val = node.data;
        node.data = parent_node.data;
        parent_node.data = saved_val;
        if (parent_node.parent_node) {
            this.place_value_recurse(parent_node, parent_node.parent_node);
        }
    }
}

// Add a value to the heap. This method will add a node to the next
// empty spot from a top-down left-to-right orientation, and then
// will swap values with it's parent until each parent is less than
// it's child
Heap.prototype.add_value = function(data) {
    var node = new Node(data);
    if (!this.current_node.left) {
        node.parent_node = this.current_level[this.current_ind];
        this.current_node.left = node;
    } else {
        node.parent_node = this.current_level[this.current_ind];
        this.current_node.right = node;
        // If we run out of nodes on the current level, build
        // out the next level.
        this.current_ind++;
        if (this.current_ind === this.current_level.length) {
            this.current_ind = 0;
            next_level = [];
            for (x = 0; x < this.current_level.length; x++) {
                next_level.push(this.current_level[x].left);
                next_level.push(this.current_level[x].right);
            }
            this.current_level = next_level;
            this.set_current_node();
        }
    }

    // Switch values with parents until descending order is restored
    this.place_value_recurse(node, node.parent_node);
}

// Tests
var results = {successes: 0, failures: 0};
testHeap = function(input) {
    var root = new Node(6);
    var heap = new Heap(root);
    heap.add_value(7);
    heap.add_value(4);
    console.log(heap);
}
testHeap();

console.log(`${results.successes} successes, ${results.failures} failures.`);

