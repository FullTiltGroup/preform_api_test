from formlabs_sdk import FormlabsClient

with FormlabsClient() as client:
    # connect() attaches to the running PreForm and leaves its login alone. Closing
    # the client leaves PreForm running.
    preform = client.preform.connect(base_url="http://preform-server:44388")
    user = preform.current_user()
    print(f"PreForm {preform.version} at {preform.base_url}")
    # current_user() returns None when PreForm is logged out.
    print(f"Logged in as {user.username}" if user else "Not logged in")
