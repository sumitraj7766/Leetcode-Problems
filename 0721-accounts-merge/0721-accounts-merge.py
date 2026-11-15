
class Solution(object):
    def accountsMerge(self, accounts):
        graph = {}
        email_to_name = {}

        # Step 1: Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                graph.setdefault(email, [])
                graph[email].append(first_email)
                graph[first_email].append(email)

                email_to_name[email] = name

        # Step 2: DFS to find connected components
        visited = set()
        result = []

        for email in graph:
            if email not in visited:

                stack = [email]
                visited.add(email)
                emails = []

                while stack:
                    current = stack.pop()
                    emails.append(current)

                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                # Step 3: Sort emails
                emails.sort()

                # Step 4: Add name and emails
                result.append([email_to_name[email]] + emails)

        return result
