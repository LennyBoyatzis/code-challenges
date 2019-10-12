from typing import List


def num_unique_emails(emails: List[str]) -> int:
    processed_emails = set()

    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = local_name.split('+')[0]
        local_name = local_name.replace('.', '')
        processed_emails.add('@'.join([local_name, domain_name]))
    return len(processed_emails)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    result = num_unique_emails(emails)
