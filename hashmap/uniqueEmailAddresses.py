class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        hashMap = {}
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local, garbage = local.split('+')
            local = local.replace('.', '')
            hashMap[local] = domain
            print(local)
            print(domain)
            print(hashMap)

        return 0
