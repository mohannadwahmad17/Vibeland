import React from 'react'
import { useState } from "react";
import { SafeAreaView, StyleSheet, TextInput } from "react-native";

const LoginPage = () => {
    const [username, onChangeUsername] = React.useState(null);
    const [password, onChangePassword] = React.useState(null);

    return (
        <SafeAreaView>
            <TextInput
                style={styles.input}
                onChangeText={onChangeUsername}
                value={username}
                placeholder="Enter Username"
            />
            <TextInput
                style={styles.input}
                onChangeText={onChangePassword}
                value={password}
                placeholder="Enter Password"
            />
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    input: {
        height: 40,
        margin: 12,
        borderWidth: 1,
        padding: 10,
    },
});

export {
    LoginPage
};