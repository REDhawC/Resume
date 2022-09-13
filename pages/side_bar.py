import dash
from dash import html
import dash_bootstrap_components as dbc
SIDEBAR_STYLE = {
    "backgroundColor": "whitesmoke",
    "width": "15rem",
    "right": 150,
}

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/kaggle1"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div('Kaggle competition: H&M Personalized Fashion Recommendations', className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/projects":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Financial Dashboard web app", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/kaggle2":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div('Kaggle Competition: NBME - Score Clinical Patient Notes', className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/kagsrt":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div('The effect of blockchain on stock price crash risk: quantitative research', className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="page-link",
                   style=SIDEBAR_STYLE)