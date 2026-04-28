class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splitted = path.split("/")
        filtered_path = [p for p in path_splitted if p]
        stack = []
        for p in filtered_path:
            if p == "..":
                if stack:
                    stack.pop()
            elif p == ".":
                continue
            else:
                stack.append(p)
        return "/"+"/".join(stack)
            
            
        