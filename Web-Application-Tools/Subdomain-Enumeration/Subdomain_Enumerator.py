import subprocess
import platform



print("\nSub-Domain Enumeration Tool\n")

def domain(domain_main=None):
    if domain_main is None:
        domain_main = input("Enter a domain name: ")

    common_prefix = ['www.', 'mail.', 'blog.', 'shop.', 'dev.', 'api.', 'admin.', 'app.', 'support.', 'test.']
    


    def Windows_script():
        for prefix in common_prefix:

            combined = prefix + domain_main

            try: 
                ip_combined = subprocess.check_output(["nslookup", combined], stderr=subprocess.DEVNULL)

                ip_combined = ip_combined.decode('utf-8').replace("\r", "")
                
                if "Name:" in ip_combined or "Addresses:" in ip_combined:

                    print(f"Subdomain exists: {combined}")
                else:
                    print(f"Subdomain does not exist: {combined}")

            except subprocess.CalledProcessError:
                print(f"Subdomain does not exist: {combined}")


    def Linux_script():
        for prefix in common_prefix:

            combined = prefix + domain_main

            try: 
                ip_combined = subprocess.check_output(["dig", "+short", combined], stderr=subprocess.DEVNULL)

                ip_combined = ip_combined.decode('utf-8').replace("\r", "")
                
                if ip_combined:
                    print(f"Subdomain exists: {combined}")
                else:
                    print(f"Subdomain does not exist: {combined}")

            except subprocess.CalledProcessError:
                print(f"Subdomain does not exist: {combined}")


    system = platform.system()


    if system == "Linux":
        Linux_script()
    elif system == "Windows":
        Windows_script()
    else:
        print(f"Unsupported systemL {system}")

        return domain_main