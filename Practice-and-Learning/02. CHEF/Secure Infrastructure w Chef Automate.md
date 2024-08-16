- chef automate uses inspec, which runs over the SSH protocol and thus requires no software to be installed on target system.

### Automating Correction
automated correction is important for many reasons as manual correct has several problems: 
- not portable, doesn't necessarily transfers between distributions
- tedious and time consuming by hand
- error prone 
- not documented
- not easily scalable do to previous reasons
- difficult to repeat due to lack of documentation

Auditd package helps automatically correct issues within automated software.

### Test Kitchen
- test kitchen is a temporary infrastructure to detect and correct issues

