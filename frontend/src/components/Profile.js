import { View, Text } from "react-native";
import React from "react";
import Icon from "react-native-vector-icons/FontAwesome";
import { Input, Card, Button } from "@rneui/themed";
import BootstrapStyleSheet from "react-native-bootstrap-styles";
import { useNavigation } from "@react-navigation/native";
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;
const Profile = () => {
  return (
    <View style={[s.container]}>
      <Card>
        <Card.Title>My Profile</Card.Title>
        <Card.Divider />
        
      </Card>
    </View>
  );
};

export default Profile;
