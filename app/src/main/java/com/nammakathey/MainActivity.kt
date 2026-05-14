package com.nammakathey

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.nammakathey.data.DataProvider
import com.nammakathey.databinding.ActivityMainBinding
import com.nammakathey.model.District

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.rvDistricts.layoutManager = LinearLayoutManager(this)
        binding.rvDistricts.adapter = DistrictAdapter(DataProvider.getDistricts()) { district ->
            val intent = Intent(this, HeroListActivity::class.java)

            intent.putExtra("DISTRICT_ID", district.id)
            intent.putExtra("districtImage", district.image)   // 👈 ADD THIS LINE

            startActivity(intent)
        }
        binding.btnBadges.setOnClickListener {
            val bounceAnim = android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)
            it.startAnimation(bounceAnim)
            startActivity(Intent(this, BadgeActivity::class.java))
        }

        binding.btnProfile.setOnClickListener {
            val bounceAnim = android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)
            it.startAnimation(bounceAnim)
            startActivity(Intent(this, ProfileActivity::class.java))
        }

        binding.btnBack.setOnClickListener {
            val bounceAnim = android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)
            it.startAnimation(bounceAnim)
            startActivity(Intent(this, SelectProfileActivity::class.java))
            finish()
        }
    }

    class DistrictAdapter(
        private val districts: List<District>,
        private val onClick: (District) -> Unit
    ) : RecyclerView.Adapter<DistrictAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvName: TextView = view.findViewById(R.id.tvDistrictName)
            val ivImage: android.widget.ImageView = view.findViewById(R.id.ivDistrictImage)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_district, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val district = districts[position]
            holder.tvName.text = district.name
            holder.itemView.setOnClickListener { onClick(district) }
            
            val context = holder.itemView.context
            val resourceId = context.resources.getIdentifier(district.image, "drawable", context.packageName)
            if (resourceId != 0) {
                holder.ivImage.setImageResource(resourceId)
            } else {
                holder.ivImage.setImageResource(R.drawable.ic_placeholder_hero)
            }
        }

        override fun getItemCount() = districts.size
    }
}
