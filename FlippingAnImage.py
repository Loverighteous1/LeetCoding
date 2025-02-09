from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """
        Descrpition:
            Given an n x n binary matrix image, flip the image horizontally, then invert it, 
            and return the resulting image.

            To flip an image horizontally means that each row of the image is reversed.

            For example, flipping [1,1,0] horizontally results in [0,1,1].
            To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

            For example, inverting [0,1,1] results in [1,0,0].

        Input:
        image : a list of lists, n x n binary matrix

        Return:
        Resulting image :  list of lists 
        """
        assert isinstance(image, List), "Your input must be a list"
        n = len(image)
        assert 1 <= n <= 20, "The number of lists in the list must be from 1 to 20"
        for row in image:
            assert isinstance(row, List), "Each row must be a list"
            assert len(row) == n, f"Each row length must be {n}"
            for  elt in row:
                assert elt in {0, 1}, f"Each integer must be either 0 or 1 not {elt}"

    
        flip_image = [[0]]* len(image)

        for i in range(len(image)):
                flip_image[i] = flip_image[i] * len(image[i])

        
         ### Flip each row
            
        for i in range(len(image)):
            im = image[i]
            flip_im = flip_image[i]
            for j in range(1, len(im)+1):
                flip_im[j-1] = im[-j]
            flip_image[i] = flip_im

        ### Invert each row

        invert_im = flip_image # in case I need to return the result after flipping
        for k in range(len(invert_im)):
            inv_im = invert_im[k]
            for i in range(len(inv_im)):
                if inv_im[i] == 0:
                    inv_im[i] = 1
                else:
                    inv_im[i] = 0

        return invert_im


### Test cases
image1 = ([1,1,0],[1,0,1],[0,0,0])
image2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]      
image3 = [[0, 1, 0], [1, 0, "a"]]
image4 = [[0, 1], [1, 0]]
image5 = [[0, 1], [1, -1]]

solution = Solution()


print(solution.flipAndInvertImage(image1)) # AssertionError: Your input must be a list

res = solution.flipAndInvertImage(image2)
print(res == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]) # True

print(solution.flipAndInvertImage(image3)) # AssertionError: Each row length must be 2

print(solution.flipAndInvertImage(image4)) # [[0, 1], [1, 0]]

print(solution.flipAndInvertImage(image5)) # Each integer must be either 0 or 1 not -1



