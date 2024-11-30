import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

from Lesson13.pd import header

load_dotenv()

Api_base_url = os.getenv("api_base_url")


def get_categories():
    response = requests.get(f"{Api_base_url}/categories")
    return response.json()


def get_recipes(cuisine=None, difficulty=None):
    param = {}
    if cuisine:
        param["cuisine"] = cuisine

    if difficulty:
        param["difficulty"] = difficulty

    response = requests.get(f"{Api_base_url}/recipes", params=param)

    return response.json()


def create_category(category_name):
    responses = requests.post(
        f"{Api_base_url}/categories", json={"name": category_name})
    return responses.json()


def update_category(category_id, category_name):
    response = requests.put(
        f"{Api_base_url}/categories/{category_id}", json={"name": category_name})
    return response.json()


def delete_category(category_id):
    response = requests.delete(f"{Api_base_url}/categories/{category_id}")
    return response.json()


def create_recipes(recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.post(f"{Api_base_url}/recipes", json={
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    })
    return response.json()


def update_recipe(recipe_id, recipe_name, description, ingredients, instructions, cuisine, difficulty, category_id):
    response = requests.put(f"{Api_base_url}/recipes/{recipe_id}", json={
        "name": recipe_name,
        "description": description,
        "ingredients": ingredients,
        "instructions": instructions,
        "cuisine": cuisine,
        "difficulty": difficulty,
        "category_id": category_id
    })
    return response.json()


def delete_recipe(recipe_id):
    response = requests.delete(f"{Api_base_url}/recipes/{recipe_id}")
    return response.json()

st.title("Online Reciepe Book")
menu=["Dashboard","Manage Reciepes", "Manage Categories"]
selected_menu=st.sidebar.selectbox("Menu",menu)
if selected_menu=="Dashboard":
    st.header("Dashboard")
    st.subheader("Reciepes")
    reciepe_list=get_reciepes()
    if reciepe_list:
        df_reciepes=pd/DataFrame(reciepe_list)
        if "id" in df_reciepes.columns:
            df_reciepes=df_reciepes/drop(colums=["id"])
        df_reciepes.reset_index(drop=True, inplace=True)
        df_reciepes.index+=1
        st.dataframe(df_reciepes, use_container_width=True)
    else:
        st.info("no Reciepes found.")

    st.subheader("Categories")
    category_list=get_categories()
    if category_list:
        df_categories=pd.DataFrame(category_list)
        if "id" in df_categories.columns:
            df_categories=df_categories.drop(column=["id"])
            df_categories.reset_index(drop=True,inplace=True)
            df_categories+=1
            st.dataframe(df_categories, use_container_width=True)
        else:
            st.info("No categories found")

    elif selected_menu=="Manage Reciepes":
        st,header("Manage Reciepes")
        st.subheader("Add a new Reciepie")
        reciepe_name=st.text_input("Reciepe Name", key="new_reciepe_name")
        reciepe_description=st.text_input("Reciepe description", key="new_reciepe_description")
        reciepe_ingridients=st.text_input("Reciepe ingridients", key="new_reciepe_ingridients")
        reciepe_cuisine=st.text_input("Reciepe cuisine", key="new_reciepe_cuisine")
        reciepe_difficulty=st.selectbox("Difficulty",["Easy", "Medium","Hard"])
        reciepe_instructions=st.text_input("Reciepe instructions", key="new_reciepe_instructions")

        category_list=get_categories()
        if category_list:
            category_names=[cat["name"]for cat in category_list]
            selected_categoery_name=st.selectbox("Category", category_names,key="new_reciepe_category")
            selected_categoery_id=next(cat["id"] for cat in category_list if cat["name"]==selected_categoery_name)
        else:
            st.error("Failed to retrieve categories")
            selected_category_id=None
        if st.button("Add Reciepe", key="add_recieve_button"):
            if (all([reciepe_name,reciepe_ingridients,reciepe_instructions,reciepe_cuisine,reciepe_difficulty,selected_category_id is not None])):
                create_recipes(recipe_name,reciepe_description,reciepe_ingridients,reciepe_instructions,reciepe_cuisine,reciepe_difficulty,selected_category_id)
                st.success(f"Reciepe{reciepe_name}added sucesfully")
            else:
                st.error("all fields must be filled and category selected to add a reciepe")
        st.subheader("Edit or delete reciepe")
        reciepe_list=get_recipes()
        if reciepe_list:
            reciepe_name=[reciepe["name"] for reciepe in reciepe_list]
            if manage_action=="Edit":
                reciepe_edit=st.selectbox("Select a reciepe to edit", reciepe_name, key="edit_reciepe_select")
            if manage_action=="Edit":
                reciepe_edit=st.selectbox("Select a reciepe to edit", reciepe_name,key="edit_reciepe_select")
                if reciepe_edit:
                    selected_reciepe=next(reciepe for reciepe in reciepe_list if reciepe["name"]==reciepe_edit)
                    st.subheader(f"edit reciepe:{selected_reciepe['name']}")
                    edit_name=st.text_input("Reciepe Name", value=selected_reciepe["name"],key="add_reciepe_name")
                    edit_description=st.text_input("description", value=selected_reciepe["description"],key="add_reciepe_description")
                    edit_ingridients=st.text_input("ingridients", value=selected_reciepe["ingridients"],key="add_reciepe_ingridients")
                    edit_cuisine=st.text_input("cuisine", value=selected_reciepe["cuisine"],key="add_reciepe_cuisine")
                    edit_instructions=st.text_input("instructions", value=selected_reciepe["instructions"],key="add_reciepe_instructions")
                    edit_difficulty=st.text_input("difficulty",["Easy","Medium","Hard"], index= ["Easy","Medium","Hard"].index(selected_reciepe["difficulty"]),key="add_reciepe_difficulty")
                    category_list=get_categories()
                    if category_list:
                        category_names=[cat["name"] for cat in category_list]
                        edit_category_name=st.selectbox("Category", category_names, index=category_names.index(next(cat["name"]for cat in category_list if cat["id"]--selected_reciepe["category_id"])),key="edit_reciepe_category")
                        edit_reciepe_id=next(cat["id"] for cat in category_list if cat ["name"]==edit_category_name)
                    else:
                        st.error("Failed to retrive categories")
                        edit_category_id=None

                    if st.button("Update Reciepe",key="udate_reciepe_button"):
                        if all([edit_name, edit_instructions, edit_cuisine, edit_difficulty,edit_category_id is not None]):
                            update_recipe(selected_reciepe["id"], edit_name, edit_description, edit_ingridients,edit_instructions,edit_cuisine,edit_difficulty,edit_category_id)
                        st.success(f"Reciepe updated nice!")
                        else:
                            st.error("All fields must be filled out")
            elif manage_action=="Delete":
                reciepe_to_delete=st.selectbox("Select a reciepe to delete", reciepe_name, key="delete_reciepe_selected")
                if reciepe_to_delete:
                    selected_reciepe=next(reciepe for reciepe in reciepe_list if reciepe["name"]==reciepe_to_delete)
                    if st.button(f"Delete {selected_reciepe['name']}"):
                        delete_recipe(selected_reciepe["id"])
                        st.success(f"Reciepe {selected_reciepe['name']} deleted succesfully")
    else:
        st.info("No reciepe availible to manage")
elif selected_menu=="Manage Categories":
    st.header("Manage Categories")
    st.subheader("Add a new Category")
    new_category_name=st.text_input("New Category Name", key="new_category_name")
    if st.button("Ass Category", key="add_category_button"):
        if new_category_name:
            create_category((new_category_name))
            st.success(f"Category created")
        else:
            st.error("Category Name cannot be empty")
    st.subheader("Edit or Delete Category")
    category_list=get_categories()
    if category_list:
        category_name=[category["name"] for category in category_list]
        manage_action=st.radio("Choose action",["Edit","Delete"],key="manage_category_action")
        if manage_action=="Edit":
            category_to_edit=st.selectbox("Select to edit", category_name, key="edit_cvategory_select")
            if category_to_edit:
                selected_categoery=next(category for category in category_list if category["name"]== category_to_edit)
                st.subheader("Edit Category")
                new_category_name=st.text_input("Category_name", value=selected_categoery["name"],key="edit_category_name")
                if st.button("Update Category", key="update_category_button"):
                    if new_category_name:
                        update_category(selected_categoery["id"], new_category_name)
                        st.success("Updated")
                    else:
                        st.error("Category name can not be empty")
        elif manage_action=="Delete":
            category_to_delete=st.selectbox("Select a category to delete", category_name,key="delete_category_select")
            if category_to_delete:
                selected_categoery=next(category for category in category_list if category["name"]==category_to_delete)
                if st.button(f"Deleted"):
                    delete_category(selected_categoery["id"])
                    st.success("Deleted")
else:
    st.info("no categories to manage")