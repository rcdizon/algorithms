// Snippets of this code are adapted from
// Mongan, Giguere & Kindler's Programming Interviews Exposed 3rd Ed

/**************
SELECTION SORT
Best, Average and Worst: O(n^2)
**************/

// Sort an array using a recursive selection sort.
public void selectionSortRecursive (int[] data) {
	selectionSortRecursive(data, 0);
}

private void selectionSortRecursive (int[] data. int start) {
	if (start < data.length - 1) {
		swap(data, start, findMinimumIndex(data, start));
		selectionSortRecursive(data, start+1);
	}
}

private int findMinimumIndex (int[] data, int start) {
	int minPos = start;
	for (int i = start +1; i < data.length; i++) {
		if (data[i] < data[minPos])
			minPos = i;
	}
	return minPos;
}

private void swap(int[] data, int index1, int index2) {
	if (index1 != index2) {
		int tmp = data[index1];
		data[index1] = data[index2];
		data[index2] = tmp;
	}
}


/**************
INSERTION SORT
Best: O(n)
Average and Worst: O(n^2)
**************/

// Sort an array using a simple insertion sort
public void insertionSort(int[] data) {
	for (int which = 1; which < data.length; ++which) {
		int val = data[which];
		for (int i = 0; i < which; ++i) {
			if (data[i] > val) {
				System.arraycopy(data, i, data, i+1, which-i);
				data[i] = val;
				break;
			}
		}
	}
}


/**************
QUICKSORT
Best and Average: O(nlog(n))
Worst: O(n^2)
**************/

// Sort an array using a simple but inefficient quicksort
public int[] quicksortSimple(int[] data) {
	if (data.length < 2)
		return data;
	
	int pivotIndex = data.length / 2;
	int pivotValue = data[pivotIndex];
	
	int leftCount = 0;

	// Count how many are less than the pivot
	
	for (int i = 0; i < data.length; ++i)
		if (data[i] < pivotValue) ++leftCount;

	// Allocate the arrays and create the subsets
	
	int[] left = new int[leftCount];
	int[] right = new int[data.length - leftCount - 1];

	int l = 0;
	int r = 0;
	
	for (int i = 0; i < data.length; ++i) {
		if (i== pivotIndex) continue;
	
		int val = data[i];
	
		if(val < pivotValue)
			left[l++] = val;
		else
			right[r++] = val;
	}

	// Sort the subsets
	
	left = quicksortSimple(left);
	right = quicksortSimple(right);

	// Combine the sorted arrays and the pivot back into the original array
	
	System.arraycopy(left, 0, data, 0, left.length);
	data[left.length] = pivotValue;
	System.arraycopy(right, 0, data, left.length+1, right.length);

	return data;
}

      
/**************
MERGESORT
Best, Average and Worst: O(nlog(n))
*Requires O(n) additional memory
**************/

// Sort an array using a simple but inefficient merge sort.
public int[] mergesortSimple(int[] data) {
	if (data.length < 2)
		return data;

	// Split the arrat into two subarrays of approximately equal size
	
	int mid = data.legth / 2;
	int[] left = new int[mid];
	int[] right = new int[data.length - mid];

	System.arraycopy(data, 0, left, 0, left.length);
	System.arraycopy(data, mid, right, 0, right.length);

	// Sort each subarray, then merge the result.
	
	mergesortSimple(left);
	mergesortSimple(right);

	return merge(data, left, right);
}

private int[] merge(int[] dest, int[] left, int[] right) {
	int dind = 0;
	int lind = 0;
	int rind = 0;

	// Merge arrats while there are elements in both
	while (lind < left.length && rind < right.length) {
		if (left[lind] <= right[rind]) 
			dest[dind++] = left[lind++];
		else
			dest[dind++] = right[rind++];
	}

	while (lind < left.length)
		dest[dind++] = left[lind++];

	while (rind < right.length)
		dest[dind++] = right[rind++];
	
	return dest;
}
