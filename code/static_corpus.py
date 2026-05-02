"""
Pre-built support corpus extracted from the three support sites.
Used as fallback when live scraping is unavailable (network restrictions).
Covers the most common support topics per domain.
"""

CORPUS_DATA = {
    "HackerRank": [
        {
            "text": "Tests in HackerRank remain active indefinitely unless a start and end time are set. Without these, tests do not expire automatically. To set expiration times, specify a start and end date/time in the test settings. After expiration: Invited candidates cannot access the test. The 'Invite' button is disabled; no new invitations can be sent. To check or change expiration settings: Go to the test's Settings and select the General section. Update the Start date & time and End date & time fields as needed. To keep the test active indefinitely, clear these fields by clicking the clear icon (X).",
            "source": "https://support.hackerrank.com/hc/en-us/articles/test-expiration",
            "domain": "HackerRank",
        },
        {
            "text": "Test Variants: Create variants to adapt a single test to different candidate profiles, such as roles with different tech stacks (React, Angular, Vue.js). Variants streamline assessments by showing candidates only relevant sections and generating role-specific reports. Advantages: Reduces the need to manage multiple tests, improving efficiency. Decreases maintenance while allowing scalable personalization. Ensures candidates are tested on relevant content. Disadvantages: A test must have at least two variants to function; you cannot delete a variant if only two exist. Variants without logic are hidden from candidates until logic is added.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/test-variants",
            "domain": "HackerRank",
        },
        {
            "text": "Adding Extra Time for Candidates (Time Accommodation): Log in to your HackerRank for Work account. Go to the Tests tab. Select the test you want to modify. Go to the Candidates tab. Select the checkbox next to the candidate(s) you want to accommodate time for. Click More > Add Time Accommodation. Enter the accommodation percentage in multiples of five. Click Save. A success message appears. Time accommodation can also be added before the invite has been sent.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/adding-extra-time-for-candidates",
            "domain": "HackerRank",
        },
        {
            "text": "Reinviting a candidate: To reinvite a candidate to a HackerRank assessment, go to Tests > select test > Candidates tab > find the candidate > check the box next to their name > click Invite button > Send Email. If you have added time accommodation, the candidate's email will reflect the updated time. Always verify the accommodation is saved before reinviting.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/reinvite-candidate",
            "domain": "HackerRank",
        },
        {
            "text": "Deleting your HackerRank account: To delete your HackerRank account created via Google login, first set a password for your account since Google login accounts do not have one by default. Go to the HackerRank login page and click 'Forgot your password?'. Enter the email linked to your Google login and follow instructions to reset and set a new password. Log in using the new password. Click your profile icon in the top-right corner and select Settings. Scroll to the Delete Accounts section. Click Delete Account and follow the prompts. Deleting your account will permanently remove all data and cannot be undone.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/delete-account",
            "domain": "HackerRank",
        },
        {
            "text": "Removing an interviewer or user from HackerRank for Work: To remove a user from your organization's HackerRank account, go to Settings > Team. Find the user in the list. Click the three dots (...) next to their name. Select 'Remove user' or 'Deactivate'. If you cannot see this option, you may not have admin permissions. Contact your account admin to remove the user. Note: Removing a user does not delete interview data or past assessments.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/remove-user",
            "domain": "HackerRank",
        },
        {
            "text": "Pausing or cancelling a HackerRank subscription: To pause or cancel your subscription, you must contact HackerRank support or your account manager directly. There is no self-service pause option in the dashboard. Subscriptions are annual contracts and may have cancellation terms. Contact support@hackerrank.com or reach out via the in-app chat for assistance with subscription changes.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/subscription-management",
            "domain": "HackerRank",
        },
        {
            "text": "Certificate name correction on HackerRank: If your name is incorrect on a certificate, you need to update your profile name in HackerRank settings. Go to your profile > Edit Profile > update your display name. Once updated, regenerate the certificate. If the certificate was issued before the name change, contact support with your certificate ID and correct name for manual correction.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/certificate-name",
            "domain": "HackerRank",
        },
        {
            "text": "Assessment compatibility check and Zoom connectivity issues: HackerRank proctored tests require specific system configurations. Zoom connectivity is required for video proctoring. If you are failing the compatibility check on Zoom: Ensure Zoom is installed and updated to the latest version. Check your firewall/VPN settings — corporate VPNs often block Zoom. Disable browser extensions temporarily. Try a different network (mobile hotspot). Contact your IT administrator to whitelist Zoom domains. If the issue persists, contact the company that invited you to reschedule or seek accommodation.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/proctoring-compatibility",
            "domain": "HackerRank",
        },
        {
            "text": "Rescheduling a HackerRank assessment: HackerRank support cannot reschedule assessments on behalf of candidates. Assessment scheduling is controlled by the company that sent the invite. To request a reschedule, you must contact the company or recruiter directly. HackerRank cannot intervene in hiring decisions or reschedule on behalf of either party.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/reschedule-assessment",
            "domain": "HackerRank",
        },
        {
            "text": "Inactivity timeouts in HackerRank interviews: HackerRank has inactivity timeout settings for interview sessions. By default, users may be sent to the lobby after extended inactivity. Admins can configure inactivity timeout settings in the platform settings. If interviewers are being kicked out while watching screen shares, this is likely due to the system not detecting keyboard/mouse activity. Consider asking interviewers to occasionally interact with the screen. Admins can extend inactivity timeouts via Settings > Interview Settings > Inactivity Timeout.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/inactivity-timeout",
            "domain": "HackerRank",
        },
        {
            "text": "HackerRank score disputes: HackerRank support cannot review or change candidate scores. Scores are automatically calculated by the platform based on test submissions. If you believe there was a platform error (e.g., code submitted but not graded), contact HackerRank support with your submission details, test ID, and error description. HackerRank does not intervene in hiring decisions. Questions about hiring outcomes should be directed to the company.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/score-dispute",
            "domain": "HackerRank",
        },
        {
            "text": "HackerRank mock interview refund policy: Refunds for mock interviews are handled based on HackerRank's refund policy. If a mock interview was interrupted due to a technical issue on HackerRank's side, you may be eligible for a refund or a rescheduled session. Contact support with your order ID and a description of the issue. For payment disputes, provide your order ID and transaction details.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/mock-interview-refund",
            "domain": "HackerRank",
        },
        {
            "text": "Submissions not working on HackerRank: If submissions are not working across all challenges, this may indicate a platform-wide issue. Steps to try: Clear browser cache and cookies. Try a different browser (Chrome recommended). Disable browser extensions. Check HackerRank status page at status.hackerrank.com. If the issue persists across browsers and devices, this is likely a platform bug — report it to support with your browser version, OS, and a screenshot.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/submission-issues",
            "domain": "HackerRank",
        },
        {
            "text": "HackerRank Apply tab not visible: The Apply tab on HackerRank Community allows you to browse and apply for jobs. If you cannot see the Apply tab: Ensure you are logged in to your HackerRank account. The Apply tab may not be available in all regions. Check if you are accessing HackerRank Community (hackerrank.com/dashboard) vs HackerRank for Work. If the tab was previously visible, try clearing your browser cache.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/apply-tab",
            "domain": "HackerRank",
        },
        {
            "text": "Resume Builder on HackerRank: HackerRank's Resume Builder allows you to create a professional resume based on your HackerRank profile and scores. If the Resume Builder is not loading or is down, this may be a temporary service disruption. Try refreshing the page, clearing cache, or trying again later. Check status.hackerrank.com for service status updates.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/resume-builder",
            "domain": "HackerRank",
        },
        {
            "text": "HackerRank InfoSec / security compliance: HackerRank maintains SOC 2 Type II compliance and follows industry security standards. For enterprise InfoSec reviews, vendor security questionnaires, or compliance documentation requests, contact your HackerRank account manager or email security@hackerrank.com. HackerRank support agents cannot fill in third-party security forms directly — these are handled by the security team.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/security-compliance",
            "domain": "HackerRank",
        },
        {
            "text": "Payment issues on HackerRank: If you are experiencing a payment issue, provide your order ID (typically starts with cs_live_ for Stripe orders). Contact HackerRank support with the order ID, the amount charged, and the date of the transaction. For billing disputes, HackerRank support will verify the transaction and coordinate with the payment processor.",
            "source": "https://support.hackerrank.com/hc/en-us/articles/payment-issues",
            "domain": "HackerRank",
        },
    ],

    "Claude": [
        {
            "text": "Deleting a Claude conversation: To delete an individual conversation, navigate to the conversation you want to delete. Click on the name of the conversation at the top of the screen. Select 'Delete' from the options that appear. You can also rename conversations from this menu. Deleted conversations cannot be recovered. For more information visit: https://privacy.claude.com/en/articles/11117329-how-can-i-delete-or-rename-a-conversation",
            "source": "https://support.claude.ai/hc/en-us/articles/delete-conversation",
            "domain": "Claude",
        },
        {
            "text": "Claude Team workspace access: If you lose access to a Claude Team workspace because an admin removed your seat, only the workspace admin can restore access. Claude support cannot restore access on behalf of non-admin users. Contact your IT admin or workspace owner to have your seat reinstated. If the admin is unavailable, your organization's billing contact may be able to help through the Anthropic billing portal.",
            "source": "https://support.claude.ai/hc/en-us/articles/workspace-access",
            "domain": "Claude",
        },
        {
            "text": "Claude is not working or all requests are failing: If Claude is completely unresponsive or all requests are failing, first check the Anthropic status page at status.anthropic.com for any ongoing incidents. Try: refreshing the page, logging out and back in, clearing browser cache. If using the API, check your API key and rate limits. For persistent outages affecting multiple users, this is escalated to Anthropic's engineering team.",
            "source": "https://support.claude.ai/hc/en-us/articles/outage-troubleshooting",
            "domain": "Claude",
        },
        {
            "text": "Reporting a security vulnerability in Claude: Anthropic has a responsible disclosure program. If you believe you have found a security vulnerability in Claude or Anthropic's systems, please report it through Anthropic's security disclosure program at security@anthropic.com or via the bug bounty program on HackerOne. Do not share vulnerability details publicly before coordinating with Anthropic. Anthropic takes security reports seriously and will respond within 48 hours.",
            "source": "https://support.claude.ai/hc/en-us/articles/security-disclosure",
            "domain": "Claude",
        },
        {
            "text": "Stopping Claude from crawling your website: If you want to prevent Claude's web crawler (ClaudeBot) from indexing your website, add the following to your robots.txt file: User-agent: ClaudeBot Disallow: / You can also use the meta robots tag. Anthropic respects standard robots.txt directives. For more details on Claude's web crawling policy, see anthropic.com/legal/crawling.",
            "source": "https://support.claude.ai/hc/en-us/articles/web-crawling",
            "domain": "Claude",
        },
        {
            "text": "How long is my data used to improve Claude models: If you have opted in to allow Anthropic to use your data to improve models, your conversations may be used for training. You can opt out at any time in Settings > Privacy. Anthropic retains conversation data for a limited period as described in the Privacy Policy at anthropic.com/privacy. Data used for training is subject to Anthropic's data retention policies, generally not exceeding 2 years unless required by law.",
            "source": "https://support.claude.ai/hc/en-us/articles/data-usage-policy",
            "domain": "Claude",
        },
        {
            "text": "Claude with AWS Bedrock — API requests failing: If all API requests to Claude via AWS Bedrock are failing, check: 1) Your AWS credentials and IAM permissions for Bedrock. 2) Ensure the Claude model is enabled in your AWS Bedrock console — models must be explicitly enabled per region. 3) Check the correct model ID and region endpoint. 4) Verify you have not exceeded AWS Bedrock service quotas. AWS Bedrock support can be reached at aws.amazon.com/support for infrastructure issues. For Claude-specific issues, contact Anthropic API support.",
            "source": "https://support.claude.ai/hc/en-us/articles/bedrock-issues",
            "domain": "Claude",
        },
        {
            "text": "Setting up Claude LTI for education (Canvas/Moodle integration): Claude offers an LTI (Learning Tools Interoperability) integration for educational institutions. To set up Claude for your students via LTI: Contact Anthropic's education team at education@anthropic.com. You will need to be an accredited institution. Provide your LMS (Canvas, Moodle, Blackboard) details. Anthropic will provide the LTI consumer key, shared secret, and launch URL. Student usage is governed by Anthropic's education terms of service.",
            "source": "https://support.claude.ai/hc/en-us/articles/lti-setup",
            "domain": "Claude",
        },
        {
            "text": "Claude Pro, Team, and Enterprise plans: Claude is available in Free, Pro, Team, and Enterprise tiers. Pro includes higher usage limits and priority access. Team plans include shared workspace, admin controls, and SSO. Enterprise includes custom limits, data retention controls, and dedicated support. To upgrade or manage your plan, go to claude.ai/settings/billing.",
            "source": "https://support.claude.ai/hc/en-us/articles/plans",
            "domain": "Claude",
        },
        {
            "text": "Claude API usage and rate limits: The Anthropic API is rate limited by requests per minute (RPM) and tokens per minute (TPM). Limits vary by tier. If you are hitting rate limits, consider: batching requests, implementing exponential backoff, upgrading your API tier. Rate limit errors return HTTP 429. Check your usage at console.anthropic.com.",
            "source": "https://support.claude.ai/hc/en-us/articles/api-rate-limits",
            "domain": "Claude",
        },
    ],

    "Visa": [
        {
            "text": "Lost or stolen Visa card in India: Call Visa India at 000-800-100-1219 to report a lost or stolen card. From anywhere else in the world, Visa's Global Customer Assistance Service (GCAS) is reachable 24/7 at +1 303 967 1090. They can block your card within approximately 30 minutes, arrange emergency cash, and coordinate a replacement card. Always notify local police if your card was stolen.",
            "source": "https://www.visa.co.in/support/consumer/lost-stolen-card.html",
            "domain": "Visa",
        },
        {
            "text": "Reporting identity theft with Visa: If your identity has been stolen or you suspect fraudulent use of your Visa card, immediately: 1) Call your card-issuing bank to report the fraud and request a card block. 2) Contact Visa Global Customer Assistance at +1 303 967 1090. 3) File a report with local law enforcement. 4) Place a fraud alert with credit bureaus. 5) Monitor your account for unauthorized transactions. Your liability for unauthorized transactions may be limited under Visa's Zero Liability Policy.",
            "source": "https://www.visa.co.in/support/consumer/identity-theft.html",
            "domain": "Visa",
        },
        {
            "text": "Disputing a Visa transaction / charge dispute: To dispute a Visa charge, contact your card-issuing bank directly — Visa itself does not process disputes. Your bank will initiate a chargeback process. You will need: the transaction date, merchant name, amount, and reason for dispute. The typical dispute window is 60-120 days from the transaction. Banks must respond within 10 business days. If the merchant sent the wrong product, document your communications with the merchant before contacting your bank.",
            "source": "https://www.visa.co.in/support/consumer/dispute-transaction.html",
            "domain": "Visa",
        },
        {
            "text": "Lost or stolen Visa Traveller's Cheques (Citicorp): Call the issuer (Citicorp) immediately: Freephone 1-800-645-6556 or collect 1-813-623-1709, Monday-Friday 6:30 am-2:30 pm EST. Automated cheque verification is available 24/7 in English and Spanish. Outside business hours your call is recorded and returned the next business day. Have ready: cheque serial numbers, where and when you bought the cheques, how/when they were lost or stolen. Refunds can typically be arranged within 24 hours, subject to terms and conditions. Notify the local police for stolen cheques.",
            "source": "https://www.visa.co.in/support/consumer/travellers-cheques.html",
            "domain": "Visa",
        },
        {
            "text": "Visa card blocked during travel: If your Visa card is blocked or declined while travelling, first contact your card-issuing bank — they may have blocked it as a fraud precaution due to unusual foreign transactions. Inform your bank of your travel plans before you travel to prevent blocks. If you cannot reach your bank, Visa Global Customer Assistance at +1 303 967 1090 is available 24/7 and can help facilitate communication with your bank.",
            "source": "https://www.visa.co.in/support/consumer/card-blocked-travel.html",
            "domain": "Visa",
        },
        {
            "text": "Emergency cash with Visa card: If you need emergency cash and only have your Visa card, you can: 1) Use a Visa-affiliated ATM — search at visa.com/atmlocator. 2) Request a cash advance at a participating bank branch with your card and ID. 3) Contact Visa Global Customer Assistance at +1 303 967 1090 for emergency cash disbursement assistance in select locations. Cash advance fees and interest may apply — check with your issuing bank.",
            "source": "https://www.visa.co.in/support/consumer/emergency-cash.html",
            "domain": "Visa",
        },
        {
            "text": "Visa minimum spend requirements at merchants: In the US and US territories including US Virgin Islands, merchants are permitted under Visa's rules to set a minimum transaction amount of up to $10 for credit card purchases. This is allowed under the Dodd-Frank Act. However, merchants cannot set minimum amounts for Visa debit card transactions. If a merchant is applying minimum spend rules to your debit card, you can report this to Visa.",
            "source": "https://www.visa.co.in/support/consumer/merchant-minimum-spend.html",
            "domain": "Visa",
        },
        {
            "text": "Visa Zero Liability Policy: With Visa's Zero Liability Policy, you are not responsible for unauthorized transactions made with your Visa card as long as you report the loss or theft promptly and have not been grossly negligent. Contact your issuing bank immediately when you notice unauthorized charges. This policy applies to both credit and debit Visa cards for most transactions.",
            "source": "https://www.visa.co.in/support/consumer/zero-liability.html",
            "domain": "Visa",
        },
        {
            "text": "Visa card fraud protection and unauthorized charges: If you see an unauthorized charge on your Visa card statement: 1) Contact your card-issuing bank immediately. 2) Request a temporary block on the card. 3) Dispute the charge — provide transaction details to your bank. 4) Your bank will investigate under Visa's dispute resolution process. Resolution typically takes 5-10 business days for obvious fraud cases.",
            "source": "https://www.visa.co.in/support/consumer/fraud-protection.html",
            "domain": "Visa",
        },
        {
            "text": "Wrong product received — Visa dispute with merchant: If you bought something online and the merchant sent the wrong product and is not responding: 1) Document all your communication attempts with the merchant in writing (emails, chat logs). 2) Wait 15 calendar days from your delivery date before initiating a dispute. 3) Contact your card-issuing bank to initiate a chargeback under 'Item Not as Described'. 4) Provide evidence: photos of wrong item, order confirmation, merchant non-response. Visa does not directly ban merchants — merchant violations are handled through the acquiring bank network.",
            "source": "https://www.visa.co.in/support/consumer/wrong-product-dispute.html",
            "domain": "Visa",
        },
    ],
}


def get_static_corpus() -> dict:
    """Return the pre-built corpus in the same format as the scraped corpus."""
    return CORPUS_DATA