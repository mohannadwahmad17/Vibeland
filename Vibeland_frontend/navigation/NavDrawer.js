import React, { useEffect } from "react";
import { ExplorePage } from "../pages/Explore";
import { NavigationContainer } from "@react-navigation/native";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { MainTabNavigator } from "./MainTabNavigator";

const Drawer = createDrawerNavigator();

const drawerNavStyles = {
    headerShown: false
}

const NavDrawer = ({route, navigation}) => {

    return (
        <Drawer.Navigator initialRouteName="Vibeland">
            <Drawer.Screen name="Vibeland" component={MainTabNavigator} />
        </Drawer.Navigator>
    );
};

export {
    NavDrawer
}