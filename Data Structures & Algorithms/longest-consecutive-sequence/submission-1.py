class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chains = []
        for num in nums:
            chained = False
            for chain in chains:
                if num == chain[0]:
                    chain[0] = num - 1
                    chained = True
                elif num == chain[1]:
                    chain[1] = num + 1
                    chained = True
            
            if not chained:
                new_chain = [num - 1, num + 1]
                chains.append(new_chain)

        merged_chains = self.chainMerge(chains)
        if merged_chains:
            max_chain = max(merged_chains, key=lambda i: i[1] - i[0])
            return max_chain[1] - max_chain[0] - 1
        else:
            return 0

    def chainMerge(self, chains):
        if len(chains) == 0:
            return []

        chains.sort(key=lambda i: i[0])
        merged_chains = [chains[0]]

        for chain in chains[1:]:
            # if there is an overlap, update the upper bound
            if self.hasOverlap(merged_chains[-1], chain):
                merged_chains[-1][1] = max(merged_chains[-1][1], chain[1])
            else:
                merged_chains.append(chain)

        return merged_chains

                

    def hasOverlap(self, interval_1, interval_2) -> bool:
        # start of interval 1 must be before end of interval 2
        # start of interval 2 must be before end of interval 1
        return (interval_1[0] + 1) <= interval_2[1] and (interval_2[0] + 1) <= interval_1[1]
