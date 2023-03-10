import { View, Text } from "react-native";
import React, { useContext, useState } from "react";
import Icon from "react-native-vector-icons/FontAwesome";
import { Input, Card, Button } from "@rneui/themed";
import BootstrapStyleSheet from "react-native-bootstrap-styles";
import { useNavigation } from "@react-navigation/native";
import { AuthContext } from "./context/AuthContext";
import { AxiosContext } from "./context/AxiosContext";
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;
const Profile = () => {
    const axiosContext = useContext(AxiosContext);
    const authContext = useContext(AuthContext);
  return (
    <View style={[s.container]}>
      <Card>
        <Card.Title>My Profile</Card.Title>
        <Card.Divider />
        <Button title="Logout" onPress={() => authContext.logout()} />
      </Card>
    </View>
  );
};

export default Profile;
