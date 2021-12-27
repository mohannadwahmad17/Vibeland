import React from "react";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs"
import { ExplorePage } from "../pages/Explore";
import { Giveaways } from "../pages/Giveaways";

const Tabs = createBottomTabNavigator();

const tabNavStyles = {
    headerShown: false
}

const MainTabNavigator = () => {
    return (
        <Tabs.Navigator initialRouteName="Home" screenOptions={tabNavStyles}>
            <Tabs.Screen name="Home" component={ExplorePage}/>
            <Tabs.Screen name="Giveaways" component={Giveaways}/>
        </Tabs.Navigator>
    );
};

export {
    MainTabNavigator
}