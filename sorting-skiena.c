// Snippets of this code are adabted from
// Skiena's Algorithms Design Manual 2nd Ed

/************
MERGESORT
Best, Average and Worst: O(nlog(n))
*Requires O(n) additional memory
************/

mergesort(item_type s[], int low, int high) {
	int middle; /* index of middle element */
	
	if (low < high) {
		middle = (low+high)/2;
		mergesort(s, low, middle);
		mergesort(s, middle+1, high);
		merge(s, low, middle, high);
	}
}

merge (item_type s[], int low, int middle, int high) {
	int i;			/* counter */
	queue buffer1, buffer2;	/* buffers to hold elements for merging */
	
	init_queue(&buffer1);
	init_quque(&buffer2);

	for (i=low; i<= middle; i++) enqueue(&buffer1, s[i]);
	for (i=middle+1 i<=high; i++) enqueue(&buffer2, s[i]);

	i = low;

	while (!empty_queue(&buffer1)) s[i++] = dequeue(&buffer1);
	while (!empty_queue(&buffer2)) s[i++] = dequeue(&buffer2);
}


/************
QUICKSORT
Best and Average: O(nlog(n))
Worst: O(n^2)
************/

quicksort(item_type s[], int l, int h) {
	int p;	/* index of partition */
	
	if ((h-1)>0) {
		p = partition(s,l,h);
		quicksort(s,l,p-1);
		quicksort(s,p+1,h);
	}
}

int partition(item_type[], int l, int h) {
	int i;		/* counter */
	int p;		/* pivot element index */
	int firsthigh;	/* divider position for pivot element */

	p = h;
	firsthigh = l;

	for(i=l; l<h; i++) {
		if (s[i] < s[p] {
			swap(&s[i], &s[firsthigh]);
			firsthigh++;
		}
	}

	swap(&s[p],&s[firsthigh];
	return (firsthigh);
}


/************
BINARY SEARCH
Best, Average and Worst: O(log(n))
************/

int binary_search(item_type s[], item_type key, int low, int high) {\
	int middle;	/* index of middle element */

	if(low > high)  return(-1);	/* ley not found */
	
	middle = (low + high)/2;
	if(s[middle] == key) return(middle);
	if(s[middle]] > key)
		return (binary_search(s,key,low,middle-1));
	else
		return (binary_search(s,key,middle+1,high));
}
