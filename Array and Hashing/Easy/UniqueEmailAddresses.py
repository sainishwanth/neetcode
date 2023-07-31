class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        count = 0
        lst = []
        for mail in emails:
            if '+' in mail:
                if '.' in mail[0:mail.index('@')]:
                    lst.append(mail[0:mail.index('+')].replace('.', '') + mail[mail.index('@'):])
                else:
                    lst.append(mail[0:mail.index('+')] + mail[mail.index('@'):])
            else:
                if '.' in mail[0:mail.index('@')]:
                    lst.append(mail[0:mail.index('@')].replace('.', '') + mail[mail.index('@'):])
                else:
                    lst.append(mail)
        return len(set(lst))
    
# Good Solution
class Solution2:
    def numUniqueEmails(self, emails: list[str]) -> int:
        EmailHashSet = set()
        for mail in emails:
            local, domain = mail.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            EmailHashSet.add(local+ '@' + domain)
        return len(EmailHashSet)