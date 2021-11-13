package com.example.pdapp

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.pdapp.databinding.FragmentSignupBinding

class SignupFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val binding = DataBindingUtil.inflate<FragmentSignupBinding>(inflater,
            R.layout.fragment_signup,container,false)

        binding.SignIn.setOnClickListener{ view : View ->
            view.findNavController().navigate(R.id.action_signupFragment_to_loginFragment3)
        }
        binding.CreateAcc.setOnClickListener{ view: View ->
            if(binding.nameU.text.toString().isNotEmpty() &&
                binding.EmailAddress.text.toString().isNotEmpty() &&
                binding.Ipasswd.text.toString().isNotEmpty()){
                var user = User(binding.nameU.text.toString(), binding.EmailAddress.text.toString(), binding.Ipasswd.text.toString())
                var db = DatabaseHandler(requireActivity())
                db.InsertData(user)
                view.findNavController().navigate(R.id.action_signupFragment_to_loginFragment3)
            }
            else {
                val toast = Toast.makeText(this.activity, "Please fill all fields.", Toast.LENGTH_SHORT)
                toast.show()
            }
        }
        return binding.root
    }
}