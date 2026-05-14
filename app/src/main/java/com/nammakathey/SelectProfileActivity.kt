package com.nammakathey

import android.app.AlertDialog
import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.animation.AnimationUtils
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.nammakathey.data.UserManager
import com.nammakathey.data.UserProfile
import com.nammakathey.databinding.ActivitySelectProfileBinding

class SelectProfileActivity : AppCompatActivity() {

    private lateinit var binding: ActivitySelectProfileBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySelectProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // ✅ Cute title
        binding.tvSelectTitle.text = "Who is reading today? 📖"

        loadProfiles()

        binding.btnCreateNew.setOnClickListener {
            val bounceAnim = AnimationUtils.loadAnimation(this, R.anim.bounce)
            it.startAnimation(bounceAnim)
            startActivity(Intent(this, LoginActivity::class.java))
        }
    }

    private fun loadProfiles() {
        val users = UserManager.getUsers(this)

        binding.rvProfiles.layoutManager = LinearLayoutManager(this)
        binding.rvProfiles.adapter = ProfileAdapter(
            users,
            onUserSelected = { selectedUser ->
                UserManager.setCurrentUser(this, selectedUser.id)
                startActivity(Intent(this, MainActivity::class.java))
                finish()
            },
            onUserDelete = { user ->
                showDeleteDialog(user)
            }
        )
    }

    private fun showDeleteDialog(user: UserProfile) {
        AlertDialog.Builder(this)
            .setTitle("Delete Profile 🗑️")
            .setMessage("Do you want to remove ${user.name}?")
            .setPositiveButton("Yes 😢") { _, _ ->
                UserManager.deleteUser(this, user.id)
                Toast.makeText(this, "Profile deleted", Toast.LENGTH_SHORT).show()
                loadProfiles() // refresh list
            }
            .setNegativeButton("No 😊", null)
            .show()
    }

    class ProfileAdapter(
        private val users: List<UserProfile>,
        private val onUserSelected: (UserProfile) -> Unit,
        private val onUserDelete: (UserProfile) -> Unit
    ) : RecyclerView.Adapter<ProfileAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvName: TextView = view.findViewById(R.id.tvProfileName)
            val ivAvatar: ImageView = view.findViewById(R.id.ivProfileAvatar)
            val ivDelete: ImageView = view.findViewById(R.id.ivDelete) // ✅ delete button
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_profile, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val user = users[position]

            holder.tvName.text = user.name

            if (user.avatarResId != 0) {
                holder.ivAvatar.setImageResource(user.avatarResId)
            }

            // ✅ Select profile
            holder.itemView.setOnClickListener {
                val bounceAnim = AnimationUtils.loadAnimation(holder.itemView.context, R.anim.bounce)
                it.startAnimation(bounceAnim)

                it.postDelayed({
                    onUserSelected(user)
                }, 150)
            }

            // ✅ DELETE BUTTON CLICK (easy for kids 💖)
            holder.ivDelete.setOnClickListener {
                val bounceAnim = AnimationUtils.loadAnimation(holder.itemView.context, R.anim.bounce)
                it.startAnimation(bounceAnim)
                onUserDelete(user)
            }
        }

        override fun getItemCount() = users.size
    }
}