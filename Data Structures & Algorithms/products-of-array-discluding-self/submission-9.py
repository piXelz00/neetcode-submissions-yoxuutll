class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product, zero_count = self.product_and_zero_count(nums)

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            return [total_product if num == 0 else 0 for num in nums]

        return [int(total_product / num) for num in nums]

    def product_and_zero_count(self, nums: List[int]) -> tuple:
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        return product, zero_count