import { View, Text, TextInput, StyleSheet, Button } from "react-native";
import React from "react";
import { useState } from "react";
import tw from "twrnc";
import axios from "axios";
const Register = () => {
  const momo_URL =
    "https://info307-production.up.railway.app/account/register/";
  const mtn_URL = "https://info307-production.up.railway.app/account/register-mtn/";
  const age_URL =
    "https://info307-production.up.railway.app/account/register-agent/";

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [address, setAddress] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [idNum, setIdNum] = useState("");
  //   const handleChange = (prop) => (event) => {
  //     setMtnCredentials({ ...mtnCredentials, [prop]: event.target.value });
  //   };

  const create_mtn = (event) => {
    event.preventDefault();
    axios
      .post(mtn_URL, {
        profile_pic: null,
        id_num: idNum,
        date_of_birth: null,
        place_of_birth: placeOfBirth,
        address: address,
        first_name: firstName,
        last_name: lastName,
        front_pic: null,
        rear_pic: null,
        balance: null,
        verified: null,
      })
      .then((response) => {
        console.log(response.data);
        alert("Success");
      })
      .catch((error) => {console.log(error);
	console.log(firstName);
console.log(lastName)});
  };

  return (
    <View>
      <Text style={tw.style("text-md", "text-red-500")}>Create an Account</Text>
      <TextInput
        style={styles.input}
        value={firstName}
        onChangeText={(e) => setFirstName(e)}
        placeholder="First Name"
      />
      <TextInput
        style={styles.input}
        value={lastName}
        onChangeText={(e) => setLastName(e)}
        placeholder="Last Name"
      />
      <TextInput
        style={styles.input}
        value={address}
        onChangeText={(e) => setAddress(e)}
        placeholder="Address"
      />
      <TextInput
        style={styles.input}
        value={idNum}
        onChangeText={(e) => setIdNum(e)}
        placeholder="ID Number"
      />
      <TextInput
        style={styles.input}
        value={placeOfBirth}
        onChangeText={(e) => setPlaceOfBirth(e)}
        placeholder="Place of Birth"
      />

      <Button title="Register" onPress={create_mtn} />

      {/* <TextInput
        style={styles.input}
        onChangeText={onChangeTextNumber}
        value={number}
        placeholder="useless placeholder"
        keyboardType="numeric"
      /> */}
    </View>
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

export default Register;
