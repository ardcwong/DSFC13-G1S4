import streamlit as st


st.set_page_config(layout='wide')

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Patient", "Health Care Provider", "Neither"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
request_1 = st.Page(
    "MedQuAd/medquad.py",
    title="Search for a Health Condition",
    icon=":material/help:",
    default=(role == "Patient"),
)
request_2 = st.Page(
    "FDA/fda_app.py", title="PharmaPal", icon=":material/bug_report:"
)


# respond_1 = st.Page(
#     "respond/respond_1.py",
#     title="Respond 1",
#     icon=":material/healing:",
#     default=(role == "Responder"),
# )
# respond_2 = st.Page(
#     "respond/respond_2.py", title="Respond 2", icon=":material/handyman:"
# )


# admin_1 = st.Page(
#     "admin/admin_1.py",
#     title="Admin 1",
#     icon=":material/person_add:",
#     default=(role == "Admin"),
# )
# admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")

account_pages = [logout_page]
request_pages = [request_1, request_2]
# respond_pages = [respond_1, respond_2]
# admin_pages = [admin_1, admin_2]

# st.title("Request manager")
# st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Patient", "Health Care Provider", "Neither"]:
    page_dict["Request"] = request_pages
# if st.session_state.role in ["Responder", "Admin"]:
#     page_dict["Respond"] = respond_pages
# if st.session_state.role == "Admin":
#     page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
