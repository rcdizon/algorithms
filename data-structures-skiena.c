// Snippets of this code are adapted from
// Skiena's Algorithm Design Manual 2nd Ed

/****
LISTS
****/

typedef struct list {
	item_type item;		/* data item */
	struct list *next;	/* point to successor */
} list;

list *search_list(list *l, item_type x) {
	if (l== NULL) return(NULL);

	if (l -> item == x)
		return (l);
	else
		return (search_list(l -> next, x));
}

void insert_list(list **l, item_type x) {
	list *p;	/* temporary pointer */
	
	p = malloc(sizeof(list));
	p -> item = x;
	p -> next = *l;
	*l = p;
}

list *predecessor_list(list *l, item_type x) {
	if ((l == NULL) || (l->next == NULL)) {
		// predecessor sought on null list
		return (NULL);
	}

	if ((l->next) -> item == x)
		return (l);
	else
		return (predecessor_list(l->next, x));	
}

delete_list(list **l, item_type x) {
	list *p;	/* item pointer */
	list *pred;	/* predecessor pointer */
	list *search_list(), *predecessor_list();

	p = search_list(*l, x);
	if (p != NULL) {
		pred = predecessor_list(*l, x);
		if (pred == NULL)	/* splice out of list */
			*l = p -> next;
		else
			pred->next = p->next;
		free(p);
	}
}

/***********
BINARY TREES
***********/

typedef struct tree {
	item_type item;		/* Data item */
	struct tree *parent;	/* Points to parent */
	struct tree *left;	/* Points to left child */
	struct tree *right;	/* Points to right child */
} tree;

tree *search_tree(tree *l, item_type x) {
	if (l == NULL) return(NULL);
	if (l->item == x) return(l);
	if (x < 1 -> item)
	if (x < item == x) return (search_tree(l->left, x));
	else return (search_tree(l->right x));
}
