package com.nammakathey

import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.nammakathey.data.DataProvider
import com.nammakathey.data.UserManager
import com.nammakathey.databinding.ActivityProfileBinding
import com.nammakathey.model.Hero

class ProfileActivity : AppCompatActivity() {

    private lateinit var binding: ActivityProfileBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val currentUser = UserManager.getCurrentUser(this)

        binding.tvUserName.text = currentUser?.name ?: "Explorer"
        val avatarResId = currentUser?.avatarResId ?: 0
        if (avatarResId != 0) {
            binding.ivUserAvatar.setImageResource(avatarResId)
        }

        val allHeroes = DataProvider.getDistricts().flatMap { it.heroes }
        
        val earnedBadges = allHeroes.filter { hero ->
            currentUser?.earnedBadges?.contains(hero.id) == true
        }

        binding.rvProfileBadges.layoutManager = LinearLayoutManager(this)
        binding.rvProfileBadges.adapter = ProfileBadgeAdapter(earnedBadges)

        binding.btnBack.setOnClickListener {
            finish()
        }

        binding.btnSwitchProfile.setOnClickListener {
            val intent = android.content.Intent(this, SelectProfileActivity::class.java)
            intent.flags = android.content.Intent.FLAG_ACTIVITY_NEW_TASK or android.content.Intent.FLAG_ACTIVITY_CLEAR_TASK
            startActivity(intent)
            finish()
        }

        binding.btnLogout.setOnClickListener {
            UserManager.logout(this)
            val intent = android.content.Intent(this, SelectProfileActivity::class.java)
            intent.flags = android.content.Intent.FLAG_ACTIVITY_NEW_TASK or android.content.Intent.FLAG_ACTIVITY_CLEAR_TASK
            startActivity(intent)
            finish()
        }
    }

    class ProfileBadgeAdapter(private val heroes: List<Hero>) : RecyclerView.Adapter<ProfileBadgeAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvName: TextView = view.findViewById(R.id.tvBadgeName)
            val tvDistrict: TextView = view.findViewById(R.id.tvDistrictName)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_badge, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val hero = heroes[position]
            holder.tvName.text = "${hero.name} Badge"
            
            // Find district name
            val district = DataProvider.getDistricts().find { it.heroes.contains(hero) }
            holder.tvDistrict.text = district?.name ?: "Unknown District"
        }

        override fun getItemCount() = heroes.size
    }
}
