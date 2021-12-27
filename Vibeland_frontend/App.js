/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import { Colors, DebugInstructions, Header, LearnMoreLinks, ReloadInstructions } from 'react-native/Libraries/NewAppScreen';
import { SafeAreaView, ScrollView, StatusBar, StyleSheet, Text, TextInput, useColorScheme, View } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { NavDrawer } from './navigation/NavDrawer';
import { SongWebPage } from './pages/SongWebPage';
import { NativeBaseProvider } from 'native-base';
import { ExplorePage } from './pages/Explore';
import { LoginPage } from './pages/Login';
import { StatsPage } from './pages/Stats';
import { Signup } from './pages/SignUp';
import type {Node} from 'react';
import React from 'react';

const Stack = createNativeStackNavigator();

const stackNavStyles = {
  headerShown: false
}

const App: () => Node = () => {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <NativeBaseProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="LoginPage" screenOptions={stackNavStyles}>
          <Stack.Screen name="LoginPage" component={LoginPage} />
          <Stack.Screen name="Home" component={NavDrawer} />
          {/* <Stack.Screen name="ExplorePage" component={ExplorePage} /> */}
          <Stack.Screen name="SongWebPage" component={SongWebPage} />
        </Stack.Navigator>
      </NavigationContainer>
    </NativeBaseProvider>
  );
};

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});

export default App;
